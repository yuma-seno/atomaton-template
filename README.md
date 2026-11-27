# atomaton-template

atomaton の配布物（`.github/` 一式）をそのまま導入した、上流の新リリースを監視するための専用リポジトリ。

- 導入バージョン: **v0.27.0**（`.github/atomaton-release.json` に記録）
- 新リリースの検出は `.github/workflows/atomaton-new-release.yml` が毎日自動で行う

## 必要なシークレット（未設定）

以下はリポジトリの Secrets に手動で設定すること。

- `ORCAROUTER_API_KEY` — エージェント実行用
- `ATOMATON_UPDATE_TOKEN` — アップデートを自動で取り込む場合に必要（Contents / Pull requests の読み書き＋Workflows の書き込み権限を持つ PAT）

シークレットなしでも新リリースの検出（通知 Issue）までは動く。

## 初期設定の手順（このリポジトリの作り方）

1. リポジトリを作成する。
2. atomaton の最新リリースから `atomaton-delivery.zip` を取得し、展開した `.github/` をリポジトリのルートに配置してコミットする。導入バージョンは `.github/atomaton-release.json` に記録される。
3. リポジトリ設定（Settings → General → Pull Requests）:
   - マージ方法は **Merge commit のみ**（Squash / Rebase は無効化）
   - **Automatically delete head branches** を有効化
4. Actions 設定（Settings → Actions → General → Workflow permissions）:
   - **Read and write permissions** を選択
   - **Allow GitHub Actions to create and approve pull requests** を有効化
5. ブランチルールセットで `main` に必須チェック `atomaton-check` を設定する（上流 atomaton 本体の構成）。
   - **このリポジトリでは未適用**：private リポジトリ＋無料プランではルールセットが使えない（GitHub Pro への移行かリポジトリの公開が必要）。監視専用のため実害は小さいが、PR のチェック必須化は効いていない点に注意。
6. `.github/atomaton/config.yaml` の `environment.setup_commands` をプロジェクトに合わせて設定する。エージェントに作業させるリポジトリでは必須。このテンプレートは監視専用なので未設定。

## 適用済みの状態

- [x] 配布物 v0.27.0 の配置（`.github/` 一式）
- [x] マージ方法：Merge commit のみ／head ブランチ自動削除
- [x] Workflow permissions：Read and write／PR の作成・承認を許可
- [ ] ブランチルールセット（上記の制約により未適用）
- [ ] シークレット2件（手動設定待ち）
