from odoo import models, fields, api, exceptions
import re

class ResUsers(models.Model):
    _inherit = 'res.users'

    def _check_name_format(self, name):
        """
        Check that each word in the 'name' field has exactly one uppercase letter at the start
        and the rest are lowercase letters.
        """
        if name:
            # Split name into words and check each word's capitalization
            words = name.split()
            for word in words:
                if not re.fullmatch(r'[A-Z][a-z]*', word):  # Match a single uppercase followed by lowercase
                    raise exceptions.UserError(
                        "El nombre es incorrecto. Verifique: '%s'" % word
                    )

    @api.model
    def create(self, vals):
        """
        Override the create method to ensure the name validation also occurs on user creation.
        """
        if 'name' in vals:
            self._check_name_format(vals.get('name'))
        return super(ResUsers, self).create(vals)

    def write(self, vals):
        """
        Override the write method to ensure the name validation occurs when the name is updated.
        """
        if 'name' in vals:
            self._check_name_format(vals.get('name'))
        return super(ResUsers, self).write(vals)