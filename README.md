# Automatic Scoring and Progression (correct and time based)

An Anki add-on which automatically scores reviews and progresses.

## Features

- For typed cards:
  - Automatically highlights one of the three/four buttons for you based on time taken
  - Automatically selects highlighted button after 4 seconds (unless you select another first)
- For non-typed cards:
  - Does nothing

## Scoring

| Correct | Time | Button |
|---|---|---|
| No | Any | Again |
| Yes | 0-4 s | Easy |
| Yes | 4-8 s | Good |
| Yes | >8 s | Hard |

## Comparison with other add-ons

- [Automatic Scoring sets the default grade (easy, good, hard &again) based on time](https://ankiweb.net/shared/info/1765221856) - does not show selected option (Anki focus bug rather than add-on bug I believe), does not progress automatically
- [SMART SPACEBAR: automatic ease scoring](https://ankiweb.net/shared/info/490202012) - does not rate things "Again", does not show selected option, does not progress automatically
- [CRUISE CONTROL: hands-free review](https://ankiweb.net/shared/info/1782540286) - does not rate things "Again" or "Hard", does not show selected option

## Compatibility with other add-ons

- [Large and Colorful Buttons](https://ankiweb.net/shared/info/1829090218) - behaviour works but button highlight is not visible
- [The KING of Button Add-ons](https://ankiweb.net/shared/info/374005964) - behaviour works but button highlight is not visible
