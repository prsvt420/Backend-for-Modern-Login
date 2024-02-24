from users.services import RegistrationService, LoginService


class AuthFacade:

    @staticmethod
    def login_or_register_user(request, *args, **kwargs):
        if AuthFacade.is_registration_request(request):
            return RegistrationService.as_view()(request)
        return LoginService.as_view()(request)

    @staticmethod
    def is_registration_request(request):
        return 'password2' in request.POST
