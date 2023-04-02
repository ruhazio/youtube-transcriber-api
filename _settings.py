from youtube_transcript_api.formatters import *

TRANSCRIPT_OUTPUT_TYPES = {
    "json": JSONFormatter(),
    "text": TextFormatter(),
    "vtt": WebVTTFormatter(),
    "srt": SRTFormatter(),
}

LANGUAGE_CODES = [
    "en",
    "es",
    "pt",
    "hi",
    "ko",
    "zh-Hans",
    "zh-Hant",
    "fr",
    "ar",
    "bn",
    "ru",
    "id",
    "af",
    "ak",
    "sq",
    "am",
    "hy",
    "as",
    "ay",
    "az",
    "eu",
    "be",
    "bho",
    "bs",
    "bg",
    "my",
    "ca",
    "ceb",
    "co",
    "hr",
    "cs",
    "da",
    "dv",
    "nl",
    "eo",
    "et",
    "ee",
    "fil",
    "fi",
    "gl",
    "lg",
    "ka",
    "de",
    "el",
    "gn",
    "gu",
    "ht",
    "ha",
    "haw",
    "iw",
    "hmn",
    "hu",
    "is",
    "ig",
    "ga",
    "it",
    "ja",
    "jv",
    "kn",
    "kk",
    "km",
    "rw",
    "kri",
    "ku",
    "ky",
    "lo",
    "la",
    "lv",
    "ln",
    "lt",
    "lb",
    "mk",
    "mg",
    "ms",
    "ml",
    "mt",
    "mi",
    "mr",
    "mn",
    "ne",
    "nso",
    "no",
    "ny",
    "or",
    "om",
    "ps",
    "fa",
    "pl",
    "pa",
    "qu",
    "ro",
    "sm",
    "sa",
    "gd",
    "sr",
    "sn",
    "sd",
    "si",
    "sk",
    "sl",
    "so",
    "st",
    "su",
    "sw",
    "sv",
    "tg",
    "ta",
    "tt",
    "te",
    "th",
    "ti",
    "ts",
    "tr",
    "uk",
    "ur",
    "ug",
    "uz",
    "vi",
    "cy",
    "fy",
    "xh",
    "yi",
    "yo",
    "zu ",
]