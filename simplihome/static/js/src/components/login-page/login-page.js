define(["knockout", "text!./login-page.html"], function(ko, loginTemplate) {
    function LoginViewModel(route) {
        var self = this;

        self.username = ko.observable();
        self.password = ko.observable();

        self.login = function() {
        }
    }
    return { viewModel: LoginViewModel, template: loginTemplate };
});
