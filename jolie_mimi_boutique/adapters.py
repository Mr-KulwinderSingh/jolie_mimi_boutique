from allauth.account.adapter import DefaultAccountAdapter

class NoPrefixAccountAdapter(DefaultAccountAdapter):
    def format_email_subject(self, subject):
        # Simply return the subject without adding [site_name]
        return subject
