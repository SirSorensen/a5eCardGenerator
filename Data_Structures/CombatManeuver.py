from Web.a5eScraper import a5e_scrape_source_text


class CombatManeuver:
    def __init__(self,
            name: str        = "", summary: str      = "",
            description: str = "", points: int       = 0 ,
            action_type: str = "", degree: str       = "",
            tradition: str   = "", prerequisite: str = ""
            ):

        # Name = "*"
        self.name = name
        
        # Summary = "*"
        self.summary = summary

        # Description = "*"
        self.description = description

        # Points = 0, 1, 2, 3, 1-3
        self.points = points
        
        # Action Type = Action, Bonus Action, Bonus Action (Stance), Reaction, Other
        self.action_type = action_type

        # Degree: Basic manuever, 1st degree, 2nd degree, 3rd degree, 4th degree, 5th degree
        self.degree = degree

        # Tradition: None, Adamant Mountain, Arcane Knight, Beast Unity, Biting Zephyr, Eldritch Blackguard, Mirror’s Glint, Mist and Shade, Rapid Current, Razor’s Edge, Sanguine Knot, Spirited Steed, Tempered Iron, Tooth and Claw, Unending Wheel
        self.tradition = tradition

        # Prerequisite: "*"
        self.prerequisite = prerequisite
    
def scrape_combat_manuever(combat_manuever_node_id:int):
    a5e_scrape_source_text(str(combat_manuever_node_id), "node/", r"Outputs\\Combat Maneuvers\\")
    