"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
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
Once_upon_a_time = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a 
    large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

When_the_going_gets = Story(
    ["adjective", "verb_1", "verb_2", "verb_3", "noun", "person", "verb_ending_in_ed"],
    """When the going gets {adjective} {verb_1} as fast as you can until you can't {verb_2} any more, and then {verb_3} down on the {noun}. {person} says you've {verb_ending_in_ed} it."""
)

stories_list = {"Once_upon_a_time": Once_upon_a_time, "When_the_going_gets": When_the_going_gets}