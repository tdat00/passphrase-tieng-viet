"""Đọc nguồn ở RAM, chỉ lưu metadata; không giữ văn bản từ điển."""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "tt1_probe", Path(__file__).with_name("tt1-probe.py")
)
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)
original_save = probe.save_tsv


def save_metadata(path, rows):
    original_save(path.with_name(path.name.replace("tt1-", "km1-")), rows)


probe.save_tsv = save_metadata
probe.GROUPS = {
    "h7a": "áo ngự|báng|bẽ mặt|bê bối|căn cứ|chàm|chăn dắt|chầu|chủng|chứng|cô đồng|cơ động|công đoàn|còng",
    "h7b": "cuồng|cưỡng|điểm nhãn|diễu hành|đình|đổ bác|động dục|động đực|ghèn|ho hắng|hở hang|hoàng đạo|hoảng sợ|khạc",
    "h7c": "khụy|khuỵ|làm khổ|lôi thôi|mất nước|nang|nạng|ngập|nghẻo|niệu|nòng|ống thở|quyền|ranh|rúng động",
    "h7d": "thiêu|thỉnh|tịch|tiên lượng|tinh tử|tong|tông|tống|trần|trận|triều|truồng|trượng|vật vã",
    "h5a": "bảng hiệu|bản hiệu|bội phát|bộc phát|bột phát|chun|thun|cột mốc|cột mốt|dí dỏm|rí rỏm|giỡn|rỡn|giun|dun|hạt dẻ|hạt giẻ|hì hục|hì hụi|lăn tăn|lăm tăm",
    "h5b": "lằng nhằng|loằng nhoằng|lon ton|long tong|lòng vòng|lòng dòng|nuốt chửng|nuốt trửng|ọp ẹp|ọt ẹt|qua quýt|qua quít|rậm rạp|giậm giạp|ròng rã|ròn rã|ru rú|giu giú|sền sệt|sềnh sệch",
    "h5c": "tép riu|tép diu|theo dõi|theo rõi|thư giãn|thư dãn|xà bông|sà bông|xanh|sanh",
    "entrants": "làm cỏ|thay lòng|mang máng|màng màng|xoành xoạch|xành xạch|xoàn xoạt|thụp|chụp|thụt|loáng thoáng|loáng choáng|rướn|dướn|rướm|xầm xì|sầm sì",
    "k2": probe.GROUPS["critical"] + "|ngọng|thâm hiểm|cắn cấu|bán thân",
}

if __name__ == "__main__":
    probe.main()
