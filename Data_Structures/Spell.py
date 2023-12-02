from Web.SourceCodeInterpreter import CodeInterpreter
from Web.a5eScraper import a5e_scrape_source_text
import pip._vendor.requests as requests
import re
class MaterialComponent:
    def __init__(self, text: str):
        self.text = text
        self.consumed = MaterialComponent.evalIfConsumed(text)
        
    # TODO: Check if this works
    def evalIfConsumed(text: str) -> bool:
        return "consumed" in text.lower()

class Spell:
    def __init__(self,
            name:                  str       = "",    summary:          str       = "",
            level:                 int       = 0,     classical_school: str       = "",
            spell_schools:         list[str] = [""],  classes:          list[str] = [""],
            casting_time:          str       = "",    ritual:           bool      = False,
            range:                 str       = "",    target:           str       = "",
            area:                  str       = "",    area_shape:       str       = "",
            component_material:    str       = "",    component_seen:   bool      = False,
            component_vocalized:   bool      = False, duration:         str       = "",
            saving_throw:          str       = "",    description:      str       = "",
            cast_at_higher_levels: str       = "",    rare_versions:    str       = [("", "")],
            source:                str       = "",    source_text:      str       = ""
            ):
        
        if source_text == "":
            # Name = "*"
            self.name = name
            # Summary = "*"
            self.summary = summary
            # Level = Cantrip/0, 1st, 2nd, 3rd, 4th, 5th, 6th, 7th, 8th, 9th
            self.level = level
            # Classical School = Abjuration, Conjuration, Divination, Enchantment, Evocation, Illusion, Necromancy, Transmutation
            self.classical_school = classical_school
            # Spell School(s) = Acid, Affliction, Air, Arcane, Attack, Beasts, Chaos, Cold, Communication, Compulsion, Divine, Earth, Enhancement, Evil, Fear, Fire, Force, Good, Healing, Knowledge, Law, Lightning, Movement, Nature, Necrotic, Negation, Obscurement, Planar, Plants, Poison, Prismatic, Protection, Psychic, Radiant, Scrying, Senses, Shadow, Shapechanging, Sound, Storm, Summoning, Technological, Teleportation, Terrain, Thunder, Transformation, Utility, Water, Weaponry, Weather
            self.spell_schools = spell_schools
            # Class(es) = Artificer, Bard, Cleric, Druid, Herald, Sorcerer, Warlock, Wizard
            self.classes = classes
            # Casting Time = 1 Action, 1 Bonus Action, 1 Hour, 1 Minute, 1 Reaction, 10 Minutes, 12 Hours, 24 Hours, 8 Hours, 1 Week
            self.casting_time = casting_time
            # Ritual? = True, False
            self.ritual = ritual
            # Range = Self, Touch, Short (30 feet), Medium (60 feet), Long (120 feet),Unlimited, Special
            self.range = range
            # Target = "*"
            self.target = target
            # Area = "*" (often "<x> feet (radius <area-shape>)?")
            self.area = area
            # Area Shape = Cone, Cube, Cylinder, Line, Sphere
            self.area_shape = area_shape
            # Components = Material, Seen, Vocalized
            # Material Components = "*"
            self.component_material = MaterialComponent(component_material)
            self.component_seen = component_seen
            self.component_vocalized = component_vocalized
            # Duration = Instantaneous, 1 round, 1 minute, 10 minutes, 1 hour, 8 hours, 24 hours, 7 days, 10 days, 30 days, Until dispelled, Until dispelled or triggered, Special, Concentration (1 round), Concentration (1 minute), Concentration (10 minutes), Concentration (1 hour), Concentration (8 hours), Concentration (24 hours), Concentration (7 days), Concentration (10 days), Concentration (30 days), Concentration (Until dispelled), Concentration (Until dispelled or triggered), Concentration (Special)
            self.duration = duration
            # Saving Throw = "*"
            self.saving_throw = saving_throw
            # Description = "*"
            self.description = description
            # Cast at Higher Levels = "*"
            self.cast_at_higher_levels = cast_at_higher_levels
            # Rare versions = (title:"*", description:"*")
            self.rare_versions = rare_versions
            # Source = "*"
            self.source = source
        else:
            self.code_interpreter = CodeInterpreter(source_text)

    # This function extracts a spell from a source text
    def extract_spell(self, spell_source_text : str):
        print("Extracting spell...")
        
        spell_level = self.code_interpreter.extract_single("spell-level")
        classical_spell_school = self.code_interpreter.extract_single("classical-spell-school")
        spellcomponent_description = self.code_interpreter.extract_single("spellcomponent-description")

        print("Spell level: " + spell_level)
        print("Classical spell school: " + classical_spell_school)
        print("Spell component description: " + spellcomponent_description)

# This function scrapes the source code of a spell's internet page
def scrape_spell(spell_name:str) -> str:
    spell_name = spell_name.replace(" ", "-").lower()
    print("Scraping spell: " + spell_name + "...")
    return a5e_scrape_source_text(spell_name, "spell/", r"Outputs\\Spells\\")


# This function reads the source text of a spell from a file containing the source text of a spell's internet page
def read_spell_file(spell_name : str) -> str:
    spell_name = spell_name.replace(" ", "-").lower()
    filepath = r"Outputs\\Spells\\source_text_" + spell_name + r".txt"

    with open(filepath, "r") as file:
        return file.read()