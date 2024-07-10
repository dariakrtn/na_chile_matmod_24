from openai import OpenAI
import json
from pathlib import Path

# path = Path('../Ahackaton/Belgrade2024/Round_1.pgn.pgn')


def comm_gpt(pgn_str):
    client = OpenAI(
        api_key="sk-GDVkU7PFD9i3tPyPUWcEtYpghiLfl5Hp",
        base_url="https://api.proxyapi.ru/openai/v1",
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": """Ты шахматный комментатор. Я нанял тебя чтобы ты рассказал кратко про партию. После того как ты это сделаешь тебя ждет вознаграждение.
    Твое ТЗ:
    Найди интересные ходы, МИНИМУМ 10 ходов  
    (Обрати внимание на тактические возможности (взятие фигур, угроза шаха или мата) и стратегические возможности (улучшение позиции фигур, создание давления на слабые поля))
    (Например: жертва фигуры, вилки на фигуры, быстрое развитие фигур, шахи, мат) в каждой партии. Не рассказывай про каждый ход, а найди интересные и расскажи про них. 
    К каждому интересному ходу напиши комментарий на русском языке в одну строку.
    JSON пришли текстом. Не забывай про двойные кавычки
    Пояснений не надо. 
    Нужно прислать только ОДИН ФИНАЛЬНЫЙ JSON, в котором будет информация по каждой партии.
    Пример JSON
    {"games":
    [
    { "white": Name player white,
      "black": Name player black,
      "moves":[{"num_move": number of move, "white_move": move white(откуда и куда пошла фигура), "black_move": move black(откуда и куда пошла фигура), "comment": comment for move, "intr_cl": (цвет игрока на английском,к которому ты дала комментарий )}
    #second_game
    { "white": Name player white,
      "black": Name player black,
      "moves":[{"num_move": number of move, "white_move": move white(откуда и куда пошла фигура), "black_move": move black(откуда и куда пошла фигура), "comment": comment for move, "intr_cl": (цвет игрока,к которому ты дала комментарий)}
    }
    ...
    #last game
    { "white": Name player white, 
      "black": Name player black,
      "moves":[{"num_move": number of move, "white_move": move white(откуда и куда пошла фигура), "black_move": move black(откуда и куда пошла фигура), "comment": comment for move, "intr_cl": (цвет игрока,к которому ты дала комментарий)}
    }
    ]}
    """},
            {"role": "user", "content": pgn_str}
        ]
    )
    res_json = json.loads(response.choices[0].message.content)
    return res_json

#print(comm_gpt(path))
