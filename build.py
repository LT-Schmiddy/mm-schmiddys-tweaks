import pathlib, subprocess, os, tomllib

mod_data = tomllib.loads(pathlib.Path("mod.toml").read_text())["manifest"]
print(mod_data)

subprocess.call("make")

subprocess.call(
    [
        "./tools/RecompModTool.exe",
        "mod.toml",
        "build"
    ],
    cwd=os.getcwd()
)

os.makedirs("./generated", exist_ok=True)
subprocess.call(
    [
        "./tools/OfflineModRecomp.exe",
        "build/mod_syms.bin",
        "build/mod_binary.bin",
        "Zelda64RecompSyms/mm.us.rev1.syms.toml",
        "generated/mod_recompiled.c",
    ],
    cwd=os.getcwd()
)

# Compile DLL:
subprocess.call(
    [
        "clang-cl", 
        "generated/mod_recompiled.c", 
        "-fuse-ld=lld", 
        "-Z7",
        "/Ioffline_build",
        "/Imm-decomp/include",
        "/Imm-decomp/overlays/gamestates/ovl_file_choose/",
        "/MD",
        "/O2",
        "/link",
        "/DLL", 
        f"/OUT:build/{mod_data['id']}-{mod_data['version']}.dll"
    ]
)