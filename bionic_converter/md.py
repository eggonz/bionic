import itertools
import math
import re


def is_in_span(query_span: tuple, spans: list) -> bool:
    """Check whether query_span overlaps with any of the other spans"""
    for i, j in spans:
        if i <= query_span[0] <= j or i <= query_span[1] <= j:
            # either query_span start or end is included in the span
            return True
    return False


def get_static_spans(in_txt: str) -> list:
    """Get the spans that should not be modified"""
    # define excluded patterns
    pattern_and_group = [
        (r"\*\*[^*]*\*\*", 0),  # already bold
        (r"`[^`\n]*`", 0),  # inline code
        (r"```[^`]*```", 0),  # code block
        #(r"[*-]\s[^\n]*\n+(((\t{2}|\s{8}).*\n)+)", 1),  # double tab after a list item = code block
        #(r"\n\w.*\n+(((\t{1}|\s{4}).*\n)+)", 1),  # single tab after a paragraph = code block
        (r"(>\s)*[*-]\s[^\n]*\n+(>\s)*(((\t{2}|\s{8}).*\n)+)", 3),  # double tab after a list item = code block (optional quote block)
        (r"\n(>\s)*\w.*\n+(>\s)*(((\t{1}|\s{4}).*\n)+)", 3),  # single tab after a paragraph = code block (optional quote block)
        (r"\[[^\]]*\]\(([^\)]*)\)", 1),  # links
    ]
    # get spans of the matches
    spans = []
    for pat, grp in pattern_and_group:
        pattern = re.compile(pat)
        spans += [m.span(grp) for m in re.finditer(pattern, in_txt)]
    return spans


def run(in_path: str, out_path: str) -> None:
    """Run MD bionic converter"""

    # read input text
    with open(in_path, 'r') as file:
        in_txt = file.read()

    # get spans that should not be modified
    invalid_spans = get_static_spans(in_txt)

    # find all word matches
    pattern = re.compile(r"(?<=\W)[a-zA-Z'-]+(?=\W)|(?<=^)[a-zA-Z'-]+(?=\W)")
    matches = [(m.start(0), m.end(0), m.group(0)) for m in re.finditer(pattern, in_txt)]

    # preprocess and select valid words
    bionic_spans = []
    for i, j, w in matches:

        # remove non-words
        pattern = re.compile(r"^\W+$")
        if re.match(pattern, w):
            continue

        # common words or word containing 's or similar
        pattern = re.compile(r"^\w+$")
        pattern_apos = re.compile(r"^\w+\'\w+$")
        if re.match(pattern, w) or re.match(pattern_apos, w):
            half_idx = math.ceil((i + j) / 2)
            span = (i, half_idx)
            bionic_spans.append(span)
            continue

        # dashed-words are split and sub-words are considered independently
        pattern = re.compile(r"[^\-]+")
        submatches = [(m.start(0), m.end(0), m.group(0)) for m in re.finditer(pattern, w)]
        if submatches:
            for si, sj, sw in submatches:
                half_idx = i + math.ceil((si + sj) / 2)
                span = (i + si, half_idx)
                bionic_spans.append(span)
            continue

    # spans are not valid if they belong to a static group
    valid_bionic_spans = [span for span in bionic_spans if not is_in_span(span, invalid_spans)]
    bionic_idx = list(itertools.chain(*valid_bionic_spans))

    # split whole text and connect it again using "**"
    broken = [in_txt[i:j] for i, j in zip([0] + bionic_idx, bionic_idx + [len(bionic_idx)+1])]
    out_txt = '**'.join(broken)

    # write output text
    with open(out_path, 'w') as file:
        file.write(out_txt)
