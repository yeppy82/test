attendance_list = []

while True:
    print("\n=== 스터디 출석부 ===")
    print("1. 출석 기록")
    print("2. 출석 목록 보기")
    print("3. 종료")

    menu = input("메뉴를 선택하세요: ").strip()

    if menu == "1":
        date = input("날짜를 입력하세요: ").strip()
        name = input("이름을 입력하세요: ").strip()

        if date == "" or name == "":
            print("날짜와 이름은 비워 둘 수 없습니다.")
            continue

        attendance = {"date": date, "name": name}
        attendance_list.append(attendance)

        print(f"{date} / {name} 출석이 기록되었습니다.")

    elif menu == "2":
        print("\n=== 출석 목록 ===")

        if len(attendance_list) == 0:
            print("아직 출석 기록이 없습니다.")
        else:
            for i, attendance in enumerate(attendance_list, start=1):
                print(f"{i}. 날짜: {attendance['date']}, 이름: {attendance['name']}")

    elif menu == "3":
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못된 입력입니다. 1, 2, 3 중에서 선택하세요.")