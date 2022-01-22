ДЗ 1!
Чтобы запустить скрипт необходимо указать название файла, затем несколько аргументов командной строки:
1) команду, которая должна выполнятся: start, stop, stop_all
2) для start можно указать session_name - название сессии (по дефолту "one") и count_users - количество юпитеров (по дефолту 4)
3) для stop можно указать session_name - название сессии (по дефолту "one") и num_for_delete - номера юпитеров, которые необходимо оставновить (можно укзаать несколько номеров через пробел)
4) для stop_all можно ничего не указывать :) (если session_name задан не по дефолту, то необходимо указать)

Пример с дефолтным значением session_name:
**tpo2021108@environ01:~$ ./hw1.py start**

_100%|██████████████████████████████████████████████████████████████████████| 4/4 [00:01<00:00,  3.36it/s]_

**tpo2021108@environ01:~$ tmux list-window**

_0: bash* (5 panes) [800x600] [layout 37c0,800x600,0,0[800x37,0,0,0,800x37,0,38,8,800x74,0,76,6,800x149,0,151,4,800x299,0,301,2]] @0 (active)
1: base_dir_0 (1 panes) [800x600] [layout 87de,800x600,0,0,1] @1
2: base_dir_1 (1 panes) [800x600] [layout 87e0,800x600,0,0,3] @2
3: base_dir_2 (1 panes) [800x600] [layout 87e2,800x600,0,0,5] @3
4: base_dir_3 (1 panes) [800x600] [layout 87e4,800x600,0,0,7] @4_


**tpo2021108@environ01:~$ ./hw1.py stop --num_for_delete 1 2**

_[Session($0 one)]
Session 1 was killed
[Session($0 one)]
Session 2 was killed_


**tpo2021108@environ01:~$ ./hw1.py stop_all**

_one was killed_


Пример с недефолтным значением session_name:
**tpo2021108@environ01:~$ ./hw1.py start --session_name two**

_100%|██████████████████████████████████████████████████████████████████████| 4/4 [00:01<00:00,  3.25it/s]_

**tpo2021108@environ01:~$ tmux list-window**

_0: bash* (5 panes) [800x600] [layout 37c0,800x600,0,0[800x37,0,0,0,800x37,0,38,8,800x74,0,76,6,800x149,0,151,4,800x299,0,301,2]] @0 (active)
1: base_dir_0 (1 panes) [800x600] [layout 87de,800x600,0,0,1] @1
2: base_dir_1 (1 panes) [800x600] [layout 87e0,800x600,0,0,3] @2
3: base_dir_2 (1 panes) [800x600] [layout 87e2,800x600,0,0,5] @3
4: base_dir_3 (1 panes) [800x600] [layout 87e4,800x600,0,0,7] @4_


**tpo2021108@environ01:~$ ./hw1.py stop --session_name two --num_for_delete 1 2**

_[Session($0 two)]
Session 1 was killed
[Session($0 two)]
Session 2 was killed_


**tpo2021108@environ01:~$ tmux list-window**

_0: bash* (5 panes) [800x600] [layout 37c0,800x600,0,0[800x37,0,0,0,800x37,0,38,8,800x74,0,76,6,800x149,0,151,4,800x299,0,301,2]] @0 (active)
3: base_dir_2 (1 panes) [800x600] [layout 87e2,800x600,0,0,5] @3
4: base_dir_3 (1 panes) [800x600] [layout 87e4,800x600,0,0,7] @4_


**tpo2021108@environ01:~$ ./hw1.py stop_all --session_name two**

_two was killed_
