me = {"height": 175,
      "like_color": "green",
      "fav_creater": "Tatsuki"
      }

key = input('type a key:')
if key in me:
    result = me[key]
    print(result)
