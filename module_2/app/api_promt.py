from openai import OpenAI
import json
from pathlib import Path



# path = Path('./Ahackaton/Belgrade2024/Round_4.pgn.pgn')


def comm_gpt(pgn_str):
    client = OpenAI(
        api_key="sk-TnXDNlNp0tVnEuVI18883U3vrnCKTdpu",
        base_url="https://api.proxyapi.ru/openai/v1",
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": """Ты шахматный комментатор. Я нанял тебя чтобы ты рассказал кратко про партию. После того как ты это сделаешь тебя ждет вознаграждение.
    Твое ТЗ:
    Найди интересные ходы, МИНИМУМ 10 ходов  (Например: жертва фигуры, вилки на фигуры, быстрое развитие фигур, шахи, мат, дебют, рокировка) в каждой партии. Не рассказывай про каждый ход, а найди интересные и расскажи про них. К каждому интересному ходу напиши комментарий.
    JSON пришли текстом
    Пояснений не надо. 
    Нужно прислать только ОДИН ФИНАЛЬНЫЙ JSON, в котором будет информация по каждой партии.
    Пример JSON
    {"games":
    [
    { "white": Name player white,
      "moves":[{"num_move": number of move, "white_move": move white, "black_move": move black, "comment": comment for move}
    #second_game
    { "white": Name player white, #first_game
      "moves":[{"num_move": number of move, "white_move": move white(откуда и куда пошла фигура), "black_move": move black(откуда и куда пошла фигура), "comment": comment for move}
    }
    ...
    #last game
    { "white": Name player white, #first_game
      "moves":[{"num_move": number of move, "white_move": move white(откуда и куда пошла фигура), "black_move": move black(откуда и куда пошла фигура), "comment": comment for move}
    }
    ]}
    """},
            {"role": "user", "content": pgn_str}
        ]
    )
    res_json = json.loads(response.choices[0].message.content)
    return res_json

#comm_gpt(path)