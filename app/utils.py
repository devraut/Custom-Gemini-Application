import logging, re

def log_error(message):
    """Log an error message."""
    logger = logging.getLogger(__name__)  # fixed getLogger
    logger.error(message)

def format_response(response):
    """Format markdown-like text into HTML."""

    # Replace newlines with <br>
    response = response.replace('\n', '<br>')

    # Bold (**text** → <strong>)
    response = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', response)

    # Italic (*text* → <em>)
    response = re.sub(r'\*(.*?)\*', r'<em>\1</em>', response)

    # Headings (# heading → <h1>, ## heading → <h2>, etc.)
    response = re.sub(r'(?m)^(#+)\s*(.*)',
                      lambda m: f'<h{len(m.group(1))}>{m.group(2)}</h{len(m.group(1))}>',
                      response)

    # Ordered list (1. item → <li>item</li>)
    response = re.sub(r'(?m)^\d+\.\s*(.*)', r'<li>\1</li>', response)

    # Unordered list (- item → <li>item</li>)
    response = re.sub(r'(?m)^\-\s*(.*)', r'<li>\1</li>', response)

    # Wrap list items in <ul>
    if '<li>' in response:
        response = '<ul>' + response + '</ul>'

    # Code blocks (``` code ```)
    if "```" in response:
        parts = response.split("```")
        formatted_response = ""
        for i, part in enumerate(parts):
            if i % 2 == 1:  # odd = code
                formatted_response += f'<pre class="code-block"><code>{part}</code></pre>'
            else:  # even = normal text
                formatted_response += part
        return formatted_response

    return response
