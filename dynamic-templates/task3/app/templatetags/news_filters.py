from django import template

from datetime import datetime

register = template.Library()


@register.filter
def format_date(value):
    now = datetime.now()
    date_value = datetime.utcfromtimestamp(value)
    time_passed = now - date_value

    seconds = time_passed.seconds
    minutes = seconds / 60

    if minutes < 10:
        return 'Just written'
    elif 10 <= minutes < 60 * 24:
        return f'{int(minutes // 60)} часов назад'
    else:
        return date_value.date()


@register.filter
def format_score(rating=None):
    if rating is None:
        return 'This post does not have a score'
    else:
        if rating < -5:
            return 'Very bad'
        elif -5 <= rating < 5:
            return 'Not bad'
        else:
            return 'Good'


@register.filter
def format_num_comments(count_of_comments):
    if count_of_comments == 0:
        return 'You will be first who write a comment'
    elif 0 < count_of_comments <= 50:
        return count_of_comments
    else:
        return 'This post has more 50+ comments'


@register.filter
def format_selftext(text, count):
    splitted_text = text.split()
    if len(splitted_text) < count * 2:
        return splitted_text
    else:
        processed_text = splitted_text[:count] + ['...'] + splitted_text[-count:]
        result = ' '.join(processed_text)
        return result
