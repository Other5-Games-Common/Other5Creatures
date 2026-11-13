# Other5Creatures: its own sound class for the creature voices, instead of Other5Combat's SFX class, so the plugin
# doesn't reach into Combat. Rerunnable.
import unreal
R = unreal.AssetRegistryHelpers.get_asset_registry()
R.search_all_assets(True)
Path = "/Other5Creatures/Shared/Audio/SC_CreatureVoices"
Cls = unreal.EditorAssetLibrary.load_asset(Path) if unreal.EditorAssetLibrary.does_asset_exist(Path) else \
	unreal.AssetToolsHelpers.get_asset_tools().create_asset("SC_CreatureVoices", "/Other5Creatures/Shared/Audio", unreal.SoundClass, unreal.SoundClassFactory())
Changed = []
for P in [str(x) for x in (R.get_referencers("/Other5Combat/Audio/Classes/SFX", unreal.AssetRegistryDependencyOptions()) or [])]:
	if not P.startswith("/Other5Creatures/"):
		continue
	W = unreal.EditorAssetLibrary.load_asset(P)
	if W and hasattr(W, "set_editor_property"):
		W.set_editor_property("sound_class_object", Cls)
		unreal.EditorAssetLibrary.save_loaded_asset(W, False)
		Changed.append(P)
unreal.EditorAssetLibrary.save_loaded_asset(Cls, False)
unreal.log("OwnSoundClass: %d sounds use SC_CreatureVoices" % len(Changed))
