#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ������
���ڣ�2020.4.12
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name== 'ʯͷ' : # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
	    a=0
    if name == 'ֽ' :
	    a=2
    if name== '����' :
	    a=4
    if name=='����':
        a=3
    if name=='ʷ����':
	    a=1
    if name!= 'ʯͷ' and name != 'ֽ'and name!= '����'and name!='����'and name!='ʷ����':
	    print("Error: No Correct Name")
	    a=5
    return a # ��Ҫ���Ƿ��ؽ�� 
    #��дִ�д���,������ɺ�passɾ��

      
   


def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number == 0 :
	    c='ʯͷ'
    if number == 2 :
	    c='ֽ'
    if number == 4 :
	    c='����'
    if number==3:
        c='����'
    if number==1:
	    c='ʷ����'# ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    return c # ��Ҫ���Ƿ��ؽ�� #��дִ�д���,������ɺ�passɾ��


def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """


    print("--------����")# ���"-------- "���зָ�
    
    print("����ѡ��Ϊ��",choice_name)
    player_choice=choice_name# ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    a=name_to_number(player_choice)# ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number
    
    if a==5:
	    return
    else:
	    b=random.randrange(0,4)# ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number
    c=number_to_name(b)# ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����
    print("�����ѡ��Ķ���Ϊ��",c)# ����Ļ����ʾ�����ѡ����������

    if a==b :# ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��
	    print("���ͼ��������һ����")
    elif a==0:
        if b==4 or b==3:
            print("��Ӯ��")
        else:
	        print("�����Ӯ��")
    elif a==1:
	    if b==4 or b==0:
		    print("��Ӯ��")
	    else:
		    print("�����Ӯ��")
    elif a==2:
	    if b==0 or b==1:
		    print("��Ӯ��")
	    else:
		    print("�����Ӯ��")
    elif a==3:
	    if b==1 or b==2:
		    print("��Ӯ��")
	    else:
		    print("�����Ӯ��")
    elif a==4:
	    if b==2 or b==3:
		    print("��Ӯ��")
	    else:
		    print("�����Ӯ��")# ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�
    return choice_name #����������ʾ��дִ�д��룬������ɺ�ɾ����pass


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)


