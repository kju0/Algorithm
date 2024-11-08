def solution(numbers):
    def is_valid_binary_tree(binary):
        # 트리의 높이에 맞는 포화 이진 트리의 노드 수로 맞추기 위해 0 패딩을 추가
        length = len(binary)
        power = 1
        while (2 ** power - 1) < length:
            power += 1
        full_binary = '0' * ((2 ** power - 1) - length) + binary

        # 포화 이진 트리의 규칙을 재귀적으로 검사
        def check_tree(subtree):
            if len(subtree) <= 1:
                return True
            mid = len(subtree) // 2
            root = subtree[mid]
            # 부모 노드가 0이면서 자식 노드 중 1이 있으면 규칙 위반
            if root == '0' and ('1' in subtree[:mid] or '1' in subtree[mid+1:]):
                return False
            # 재귀적으로 좌우 서브트리 검사
            return check_tree(subtree[:mid]) and check_tree(subtree[mid+1:])

        return check_tree(full_binary)

    # 입력된 각 수를 검사하여 결과 배열 생성
    result = []
    for number in numbers:
        binary = bin(number)[2:]  # 이진수 변환 (0b 제거)
        result.append(1 if is_valid_binary_tree(binary) else 0)

    return result