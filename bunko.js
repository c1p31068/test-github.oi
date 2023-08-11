// ファイルデータ
const file = document.getElementById("example").files[0];
// フォームデータを作成
const formData = new FormData();
// avatarというフィールド名でファイルを追加
formData.append("avatar", file);
// アップロード
fetch(送信先のURL, { method: "POST", body: formData });
