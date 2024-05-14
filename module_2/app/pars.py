import chess
import chess.pgn
import pandas as pd
import json
import io


def pars_pgn(pgn_str, match_gpt):
    res = []
    svg_all = []
    #    with open(path_json) as f:
    #        match_gpt = json.load(f)
    pgn = io.StringIO(pgn_str)
    game = chess.pgn.read_game(pgn)
    while game is not None:
        num_moves = []
        mv_w = []
        mv_b = []
        times_w = []
        times_b = []
        # comm
        comm = []
        shet = 1
        n_m = 1
        board = game.board()
        headers = game.headers
        for mt in match_gpt["games"]:
            if headers.get("White", "?") in mt["white"]:
                moves_gpt = mt["moves"]
                num_gpt = [i['num_move'] for i in moves_gpt]
                break
        svg_num = {i:[] for i in num_gpt}
        for node in game.mainline():
            move = node.move
            time = node.comment
            board.push(move)
            if shet % 2 == 1:
                mv_w.append(move.uci())
                times_w.append(time.split('][')[0][5:])
                for k in range(1, 4):
                  if (n_m + k in num_gpt):
                    f = chess.svg.board(board, size=350)
                    svg_num[n_m + k].append(f)
            else:
                mv_b.append(move.uci())
                times_b.append(time.split('][')[0][5:])
                num_moves.append(n_m)
                for k in range(1, 4):
                  if (n_m + k in num_gpt):
                    f = chess.svg.board(board, size=350)
                    svg_num[n_m + k].append(f)
                if (n_m) in num_gpt:
                    for mv in moves_gpt:
                        if mv["num_move"] == (n_m):
                            comm.append(mv["comment"])
                else:
                    comm.append(None)
                n_m += 1
            shet += 1
        n_m += 1
        if len(mv_w) > len(mv_b):
            mv_b.append(None)
            times_b.append(None)
            num_moves.append(n_m)
            if (n_m) in num_gpt:
                for mv in moves_gpt:
                    if mv["num_move"] == (n_m):
                        comm.append(mv["comment"])
            else:
                comm.append(None)
        pgn_df = pd.DataFrame({
            "num_move": num_moves,
            "move_w": mv_w,
            "move_b": mv_b,
            "time_w": times_w,
            "time_b": times_b,
            "comment": comm
        })
        res.append(pgn_df)
        svg_all.append(svg_num)
        game = chess.pgn.read_game(pgn)

    return res, svg_all

# test
# k = str(open('./Round_1.pgn.pgn').read())
# pars, svg_cadr = pars_pgn(k, json.load((open('./Round_1.json', encoding="utf-8"))))
# print(pars)
