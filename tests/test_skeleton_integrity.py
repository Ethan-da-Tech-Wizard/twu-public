import ast, hashlib, json, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class SkeletonIntegrity(unittest.TestCase):
    def test_every_python_file_parses(self):
        for p in ROOT.rglob("*.py"):
            ast.parse(p.read_text(encoding="utf-8"), filename=str(p))

    def test_manifest_hashes_match(self):
        files = json.loads((ROOT / "PUBLIC_MANIFEST.json").read_text())["files"]
        for e in files:
            if e["path"] == "PUBLIC_MANIFEST.json" or e["path"].startswith("tests/"):
                continue
            self.assertEqual(hashlib.sha256((ROOT / e["path"]).read_bytes()).hexdigest(), e["sha256"], e["path"])


if __name__ == "__main__":
    unittest.main()
