#!/usr/bin/env python3
import libtmux
import os
from tqdm import tqdm
import secrets
import argparse


def start(num_users, session_name = 'one', base_dir = './'):
    """
    Запустить $num_users ноутбуков. У каждого рабочай директория $base_dir+$folder_num
    """
    server = libtmux.Server()
    try:
        session = server.new_session(session_name)
    except:
        session = server.find_where({'session_name': session_name})
    server.list_sessions()
    for i in tqdm(range(num_users)):
        token_ = secrets.token_hex(16)
        window = session.new_window(window_name=f"base_dir_{i}")
        pane = window.split_window()
        dir_ = os.path.join(base_dir,  f'session_name_{i}')
        pane.send_keys(f'mkdir {dir_}')
        pane.send_keys(f'cd {dir_}')
        pane.send_keys(f"jupyter notebook --ip 0.0.0.0 --port {10643+i} --no-browser --NotebookApp.token='{token_}' --NotebookApp.notebook_dir=''")
    #print(server.list_sessions())
    return session

def stop(session_name, num):
    """
    @:param session_name: Названия tmux-сессии, в которой запущены окружения
    @:param num: номер окружения, кот. можно убить
    """
    server = libtmux.Server()
    sessions = server.list_sessions()
    print(sessions)
    session = server.find_where({'session_name': session_name})
    session.kill_window(f'{num}')
    print(f'Session {num} was killed')


def stop_all(session_name):
    """
    @:param session_name: Названия tmux-сессии, в которой запущены окружения
    """
    server = libtmux.Server()
    session = server.find_where({'session_name': session_name})
    session.kill_session()
    print(f'{session_name} was killed')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('cm', type=str, help='cm must be start, stop or stop_all')
    parser.add_argument('--num_for_delete', default=0, nargs='*', type=int)
    parser.add_argument('--count_users', default=4, type=int)
    parser.add_argument('--session_name', default='one', type=str)
    args = parser.parse_args()

    if args.cm == 'start':
        start(args.count_users, args.session_name)
    elif args.cm == 'stop':
        #stop(args.session_name, args.num_for_delete)
        for i in range(len(args.num_for_delete)):
            stop(args.session_name, args.num_for_delete[i])
    elif args.cm == 'stop_all':
        stop_all(args.session_name)
    else:
        raise NameError('Nope, please, see the README!')
