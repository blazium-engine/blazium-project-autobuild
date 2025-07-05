# Blazium Project Autobuild

A starter project for building a starter blazium project on all platforms. The automated actions will build everything on `master` branch.

Note: The iOS build is disabled unless you set at least Apple Team ID and Apple ID.

## Getting Started

If you fork this:

- Replace `config/name` in [project.godot](project.godot) with your game name.
- Update the following in [.github/workflows/build.yml](.github/workflows/build.yml):

```yml
env:
  GAME_NAME: BlaziumGame
  BLAZIUM_VERSION: latest
  ANDROID_PACKAGE: app.blazium.game
  IOS_PACKAGE: app.blazium.game
```

For information on how to set up the secrets, refer to the [Export Blazium Game](https://github.com/blazium-engine/export-blazium-game) Github Action:

Apple Secrets:

- secrets.DISTRIBUTION_CERTIFICATE_BASE64
- secrets.ANDROID_KEYSTORE_BASE64
- secrets.BUILD_CERTIFICATE_BASE64
- secrets.P12_PASSWORD
- secrets.KEYCHAIN_PASSWORD
- secrets.DEPLOY_PROVISION_PROFILE_IOS_BASE64
- secrets.APPLE_ID
- secrets.APPLE_TEAM_ID
- secrets.APP_SPECIFIC_PASSWORD

Android Secrets:

- secrets.ANDROID_KEYSTORE_PASSWORD
- secrets.ANDROID_KEYSTORE_USER
