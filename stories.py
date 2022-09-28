"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],flask run

        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text

# Here's a story to get you started

# I am using these variable names to pass through as html ids. None of them are duplicate, but if they were, they would need enumeration.

story1 = Story(
    ["verb", "noun", "person_you_know"],
    """You really know how to {verb} up a {noun}, {person_you_know}!"""
) 

story2 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
) 

story3 = Story(
    ["a_name", "another_name", "an_animal", "a_country", "adjective", "exclamation", "adverb", "a_drink", "favorite_food"],
    """Two friends called {a_name} and {another_name} were walking their {an_animal} in the hills in 
    {a_country}. Suddenly the sky     went {adjective} and it began to snow. "{exclamation}!" said 1. 
    "What will we do?" they shouted very {adverb} and luckily were heard by a rescue team who took them 
    home where they were wrapped up to keep warm and had a drink of {a_drink} and a {favorite_food} to eat."""
) 

