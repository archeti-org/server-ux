from odoo import models


class TierValidation(models.AbstractModel):
    _inherit = "tier.validation"

    def _get_sequences_to_approve(self, user):
        all_reviews = self.review_ids.filtered(lambda r: r.status == "pending")
        my_reviews = all_reviews.filtered(lambda r: user in r.reviewer_ids)
        done_reviewers = self.review_ids.filtered(
            lambda r: r.status != "pending" and r.done_by == user)
        if done_reviewers:
            my_reviews = my_reviews.filtered(
                lambda r: not r.definition_id.enforce_one)
        # Include all my_reviews with approve_sequence = False
        sequences = my_reviews.filtered(lambda r: not r.approve_sequence).mapped(
            "sequence"
        )
        # Include only my_reviews with approve_sequence = True
        approve_sequences = my_reviews.filtered("approve_sequence").mapped("sequence")
        if approve_sequences:
            my_sequence = min(approve_sequences)
            min_sequence = min(all_reviews.mapped("sequence"))
            if my_sequence <= min_sequence:
                sequences.append(my_sequence)
        return sequences
