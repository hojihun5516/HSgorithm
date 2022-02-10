def solution(id_list, report, k):
    answer = []
    ids = {id:0 for id in id_list}
    ids_report = {id:set([]) for id in id_list}
    send_email = {id:0 for id in id_list}
    reported_list = []
    for r in report:
        datas = r.split(" ")
        ids_report[datas[0]].add(datas[1])
    for v in ids_report.values():
        for reported in v:
            ids[reported]+=1
    reported_list = [name for name,v in ids.items() if int(v)>=int(k)]

    for name,targets in ids_report.items():
        for v in targets:
            for reported in reported_list:
                if v==reported:
                    send_email[name]+=1
    answer = list(send_email.values())
    return answer
