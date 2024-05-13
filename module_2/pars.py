import chess
import chess.pgn
import pandas as pd
import json

def pars_pgn(path_pgn, path_json):
    res = []
    with open(path_json) as f:
        match_gpt = json.load(f)
    with open(path_pgn) as pgn:
        game = chess.pgn.read_game(pgn)
        headers = chess.pgn.read_headers(pgn)
        for mt in match_gpt:
            if headers.get("White", "?") in mt["game"]:
                moves_gpt = mt["moves"]
                num_gpt = [i['num_moves'] for i in moves_gpt]
                break
        print(num_gpt)
        while game is not None:
            num_moves = []
            mv_w = []
            mv_b = []
            times_w = []
            times_b = []
            # comm
            comm = []
            i = 1
            n_m = 1
            board = game.board()
            for node in game.mainline():
                move = node.move
                time = node.comment
                board.push(move)
                if i % 2 == 1:
                    mv_w.append(move.uci())
                    times_w.append(time.split('][')[0][5:])
                else:
                    mv_b.append(move.uci())
                    times_b.append(time.split('][')[0][5:])
                    num_moves.append(n_m)
                    if str(n_m) in num_gpt:
                        for mv in moves_gpt:
                            if mv["num_moves"] == str(n_m):
                                comm.append(mv["comment"])
                    else:
                        comm.append(None)
                    n_m += 1
                i += 1
            n_m += 1
            if len(mv_w) > len(mv_b):
                mv_b.append(None)
                times_b.append(None)
                num_moves.append(n_m)
                if str(n_m) in num_gpt:
                    for mv in moves_gpt:
                        if mv["num_moves"] == str(n_m):
                            comm.append(mv["comment"])
                else:
                    comm.append(None)

            print(len(num_moves), len(mv_w), len(mv_b), len(times_w), len(times_b), len(comm))
            new_row = pd.DataFrame({
                "num_move": num_moves,
                "move_w": mv_w,
                "move_b": mv_b,
                "time_w": times_w,
                "time_b": times_b,
                "comment": comm
            })
            pgn_df = pd.DataFrame(new_row)
            res.append(pgn_df)
            game = chess.pgn.read_game(pgn)

    return res

# test
# pars = pars_pgn('./Ahackaton/Belgrade2024/Round_1.pgn.pgn', './Ahackaton/Belgrade2024/Round_1.json')
# print(len(pars))
# print(pars)