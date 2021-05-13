from odoo import fields, models


class TierDefinition(models.Model):
    _inherit = "tier.definition"

    enforce_one = fields.Boolean(
        string="Enforce One",
        default=False,
        help="Enforces the validation process to be sure a user can not "
             "approve a step if he already approved one of the previous "
             "step in the current validation process.",
    )
