"""
Bài toán: Cho một chuỗi ký tự bao gồm số nguyên dương và các toán tử hai ngôi + - * /, hãy tính giá trị của biểu thức trong chuỗi.

Input: Một biểu thức dưới dạng string, mỗi toán tử và toán hạng cách nhau bằng đúng một dấu cách.
Output: Một số thực là giá trị của biểu thức. Test case đảm bảo mọi biểu thức đều hợp lệ và có giá trị là số thực.
Ví dụ:

Input: "2 * 3 - 20 / 5"
Output: 2.0
Giải thích: 2*3 - 20/5 = 6 - 4 = 2
Hướng dẫn: Nếu không có khác biệt về độ ưu tiên của phép cộng, trừ và nhân, chia, ta có thể thực hiện tính toán tuần tự đơn giản từ trái sang phải. Tuy nhiên, do các phép tính có độ ưu tiên khác nhau, ta có thể thêm các bước xử lý để thực hiện đúng thứ tự:

Duyệt biểu thức từ trái sang phải.
Nếu gặp toán tử, thực hiện các toán tử nằm trước mà có độ ưu tiên cao hơn hoặc bằng toán tử đang xét.
Cuối cùng, thực hiện tính toán trên các toán tử chưa xử lý theo thứ tự từ phải sang trái.
Quá trình này sẽ thuận tiện hơn nếu ta tách chuỗi thành mảng các phần tử và lưu danh sách các toán hạng và toán tử đã duyệt.

Ví dụ: tính giá trị biểu thức 2 * 3 - 20 / 5

Toán tử đầu tiên là *, không có toán tử nào trước nó, ta tạm thời bỏ qua.
Toán tử tiếp theo là -, có toán tử * trước nó với độ ưu tiên cao hơn => thực hiện phép nhân => biểu thức trở thành 6 - 20 / 5
Toán tử tiếp theo là /, có toán tử - trước nó nhưng độ ưu tiên thấp hơn => bỏ qua.
Đã duyệt hết biểu thức, thực hiện tính toán theo thứ tự từ phải sang trái: 6 - 20 / 5 = 6 - 4 = 2
"""

# def cal_expression(express):
#     y = express.split()

#     numbers = []
#     operation = []

#     queue = {
#         "*": 2,
#         "/": 2,
#         "+": 1,
#         "-": 1,
#     }

#     def caculate():
#         a = numbers.pop()
#         b = numbers.pop()
#         math = operation.pop()

#         if math == "+":
#             numbers.append(a + b)
#         elif math == "-":
#             numbers.append(a - b)
#         elif math == "*":
#             numbers.append(a * b)
#         elif math == "/":
#             numbers.append(a / b)

#     for x in y:
#         if x.isdigit():
#             numbers.append(float(x))
#         else:
#             while operation and queue[operation[-1]] >= queue[x]:
#                 caculate()
#             operation.append(x)

#     while operation:
#         caculate()

# if __name__ == "__main__":
#     express = input("Nhập vào biểu thức cần tính toán: ")

#     try:
#         result = cal_expression(express)
#         print(f"Kết quả: {result}")
#     except Exception as e:
#         print(f"Chương trình đang gặp lỗi {e}")

def cal_expression(express):
    try:
        return eval(express)
    except Exception as e:
        return f"Chương trình đang gặp lỗi{e}"
    
expression = input("Nhập vào biểu thức cần tính toán: ")
result = cal_expression(expression)
print(f"Kết quả là: {result}")