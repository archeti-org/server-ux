{
    "name": "Base Tier Validation Enforce One",
    "summary": "Enforce the validation process to be sure a user can not "
               "approve a step if he already approved one of the previous "
               "step in the current validation process.",
    "version": "14.0.1.0.1",
    "category": "Tools",
    "website": "https://github.com/OCA/server-ux",
    "author": "Ecosoft,Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "depends": ["base_tier_validation"],
    "data": [
        "views/tier_definition_view.xml"
    ],
    "development_status": "Alpha",
    "maintainers": ["oreju"],
    "application": False,
    "installable": True,
    "uninstall_hook": "uninstall_hook",
}
