import json


# Lesson using pytest
def simple_tdd_function (a,b):
    """Computes the sum of two integers

    Parameters
    ----------
    a : {int} a first number
    b : {int} a second number

    Returns
    -------
    int : the sum of those numbers
    """

    return (a + b)


# Exercise 1
def read_json_file (file_path):
    """Reads and parse a json file.

    Parameters
    ----------
    file_path : {str} the path to the json file.

    Returns
    -------
    dict : a dictionary containing the json structure read from the file.
    """

    json_contents = open(file_path).read()
    return dict(json.loads(json_contents))



# Exercise 2
def course_weeks_count (json_data):
    """Counts how many weeks there are in a course described in a JSON structure.

    Parameters
    ----------
    json_data : {dict} a JSON structure as read from a file using read_json_file().

    Returns
    -------
    int : the number of weeks in the course (0 if there is no weeks list)

    Notes
    -----
    look at data/course_1_full.json for an example of the structure of a course,
    here is a description of the schema of that structure:

    root (dict)
    |- key "course_id" => (str)
    |- key "weeks" => (list) of str
    |- key "content_units" => (dict) in which keys is a subset of the list found in "weeks"
                              and each entry of that dict is a list of strings
                              giving the names of the lessons.

    error cases: if the key 'weeks' doesn't exist, should return 0
    """

    if 'weeks' in json_data:
        return len(json_data['weeks'])
    else:
        return 0


# Exercise 3
def course_content_count (json_data):
    """Counts how many lessons there are in each week of a course.

    Parameters
    ----------
    json_data : {dict} a JSON structure as read from a file using read_json_file().

    Returns
    -------
    dict : a dictionary giving for each week of the course the number of lessons.

    Notes
    -----
    look at data/course_1_full.json for an example of the structure of a course,
    here is a description of the schema of that structure:

    root (dict)
    |- key "course_id" => (str)
    |- key "weeks" => (list) of str
    |- key "content_units" => (dict) in which keys is a subset of the list found in "weeks"
                              and each entry of that dict is a list of strings
                              giving the names of the lessons.

    error cases: weeks in 'content_units' that are not found in 'weeks' should not be counted
    error cases: if there is no 'weeks' in the course, return an empty dict
    """

    output = {}
    num_weeks = 0

    if 'weeks' in json_data:
        num_weeks = len(json_data['weeks'])

    for i in range(0, num_weeks):
        week = json_data['weeks'][i]
        if week in json_data['content_units']:
            output[week] = len(json_data['content_units'][week])

    return output


# Exercise 4
def tones_parse_anger (json_data):
    """Returns the probability of detection of Anger in a ToneAnalyzer json response.

    Parameters
    ----------
    json_data : {dict} a JSON structure as read from a file using read_json_file().

    Returns
    -------
    float : the probability of the detection of Anger.

    Notes
    -----
    - if no Anger is found in the json structure, should return 0.0
    - within the list given by "tone_categories", emotion is not necessarily the first
    - within the list of tones that have "category_id": "emotion_tone", Anger is not necessarily the first
    """

    result = 0

    tone_categories = json_data['document_tone']['tone_categories']
    for i in range(0, len(tone_categories)):
        tones = tone_categories[i]['tones']
        for j in range(0, len(tones)):
            tone = tones[j]
            if tone['tone_id'] == 'anger':
                result = tone['score']

    return result
