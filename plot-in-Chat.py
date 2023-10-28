import asyncio
import pandas as pd
import panel as pn
import random

from panel.chat import ChatMessage
from panel.chat import ChatInterface

# random df
df = pd.DataFrame(random.choices(range(10), k=10), columns=["A"])



vegalite = {
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "data": {"url": "https://raw.githubusercontent.com/vega/vega/master/docs/data/barley.json"},
    "mark": "bar",
    "encoding": {
        "x": {"aggregate": "sum", "field": "yield", "type": "quantitative"},
        "y": {"field": "variety", "type": "nominal"},
        "color": {"field": "site", "type": "nominal"}
    },
    "width": "container",
}
vgl_pane = pn.pane.Vega(vegalite, height=240)


chat_feed = pn.chat.ChatFeed()

feed = pn.chat.ChatFeed(
    ChatMessage(pn.widgets.Button(name="Click Here")),
    ChatMessage(df),
    ChatMessage(vgl_pane),
).servable()

feed()
