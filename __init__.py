from anki.cards import Card
from anki.utils import strip_html
from aqt import gui_hooks
from aqt.reviewer import Reviewer
from math import floor
from time import time


def get_expected(reviewer: Reviewer):
    return strip_html(reviewer.mw.col.media.strip_av_tags(reviewer.typeCorrect)).strip()


def get_actual(reviewer: Reviewer):
    return reviewer.typedAnswer.strip()


def is_correct(reviewer: Reviewer):
    if len(get_expected(reviewer)) == 0:
        return None
    return get_expected(reviewer) == get_actual(reviewer)


time_start = 0
time_limit_s = 4


def did_show_question(card: Card):
    global time_start
    time_start = time()


def will_init_answer_buttons(buttons_tuple, reviewer: Reviewer, card: Card):
    time_s = time() - time_start
    correct = is_correct(reviewer)

    if correct is None:
        button = None
    elif correct:
        # Highest button is easiest, so count down from there
        button = max(2, len(buttons_tuple) - floor(time_s / time_limit_s))
    else:
        button = 1

    print(
        f"will_init_answer_buttons: time_s={time_s} correct={correct} button={button}"
    )

    if button is not None:
        reviewer.bottom.web.eval(
            f"""
            setTimeout(() => {{
                const button = document.querySelector('button[data-ease="{button}"]')
                button.style.background = 'var(--button-primary-bg)'
                setTimeout(() => {{
                    if (document.activeElement === document.body) {{
                        button.click()
                    }} else {{
                        button.style.background = ''
                    }}
                }}, {time_limit_s}000)
            }}, 100)
            """
        )

    return buttons_tuple


gui_hooks.reviewer_did_show_question.append(did_show_question)
gui_hooks.reviewer_will_init_answer_buttons.append(will_init_answer_buttons)
