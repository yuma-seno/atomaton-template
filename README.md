# atomaton-template

atomaton の配布物（`.github/` 一式）をそのまま導入した、上流の新リリースを監視するための専用リポジトリ。

- 導入バージョン: **v0.27.0**（`.github/atomaton-release.json` に記録）
- 新リリースの検出は `.github/workflows/atomaton-new-release.yml` が毎日自動で行う

## 必要なシークレット（未設定）

以下はリポジトリの Secrets に手動で設定すること。

- `ORCAROUTER_API_KEY` — エージェント実行用
- `ATOMATON_UPDATE_TOKEN` — アップデートを自動で取り込む場合に必要
