from django.shortcuts import render, redirect
from django.views.generic import CreateView, View
from django.urls import reverse_lazy
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import PasswordChangeView
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .forms import (CustomUserCreationForm,
                    UserEditForm,
                    ProfileEditForm)
from .tokens import account_activation_token
from django.contrib import messages
from django.contrib.auth.decorators import login_required

User = get_user_model()


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/registration.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(self.request)
        mail_subject = 'Активация нового пользователя'
        message = render_to_string('users/activation/message.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(mail_subject,
                             message,
                             to=[to_email])
        email.send()
        messages.success(self.request,
                         """Проверьте указанный при регистрации email адресс.
            Мы отправили вам сообщение с дальнейшими инструкциями.""")
        return super().form_valid(form)


class ActivationView(View):
    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist) as e:
            user = None
            print(e)
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            messages.success(
                request, "Ваш профиль успешно зарегистрирован.")
            return redirect('users:profile')
        else:
            messages.warning(
                request, "Ошибка прав доступа! Возможно введены не верные данные.")
        return redirect('users:login')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(request.POST,
                                 instance=request.user)
        profile_form = ProfileEditForm(request.POST,
                                       request.FILES,
                                       instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('users:profile')
    user_form = UserEditForm(instance=request.user)
    profile_form = ProfileEditForm(instance=request.user.profile)
    context = {'user_form': user_form,
               'profile_form': profile_form}
    return render(request, 'users/profile.html', context)


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'users/passwd/change.html'
    success_url = reverse_lazy('users:profile')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Пароль был успешно изменен.")
        return super().form_valid(form)
