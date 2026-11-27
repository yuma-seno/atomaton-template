# atomaton-template

atomaton（GitHub Actions で動くエージェント配布物）を導入済みのテンプレートリポジトリです。「Use this template」からリポジトリを作ると、atomaton が入った状態で始められます。

- 導入バージョン: v0.27.0

## 作った後にやること

1. **シークレットを設定する**（Settings → Secrets and variables → Actions）
   - `ORCAROUTER_API_KEY` — エージェントの実行に必須
   - `ATOMATON_UPDATE_TOKEN` — 新リリースを自動で取り込む場合に必要（Contents / Pull requests の読み書き＋Workflows の書き込み権限を持つ PAT）
2. **リポジトリ設定を合わせる**（テンプレートからは引き継がれません）
   - Pull Requests: マージ方法は Merge commit のみ、Automatically delete head branches を有効化
   - Actions → Workflow permissions: Read and write permissions ＋ Allow GitHub Actions to create and approve pull requests を有効化
   - Rules → Rulesets → New ruleset → Import a ruleset で、同梱の `.github/atomaton/rulesets/main.json` を取り込む
3. **エージェントに初期設定を頼む**
   - 新しい Issue を作り、本文の先頭行に単独で `/atomaton` と書き、続けて「このプロジェクトに合わせて `environment.setup_commands` を設定して」など、やってほしいことを書く。エージェントが config を整えます

## LLM プロバイダーについて

プロバイダーは OrcaRouter に限定されません。エージェント定義（`.github/atomaton/agent-definitions/`）の `provider` を変更し、そのプロバイダー用の名前でシークレットを設定すれば、対応している他のプロバイダーも利用できます。

## 使い方

- エージェントへの依頼は Issue / コメントの先頭行に単独で `/atomaton` と書くのが合図です
- atomaton の新リリースは毎日自動で検知され、通知 Issue が立ちます（シークレット未設定でも検知は動きます）
