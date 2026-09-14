# Contributing

Contributions should preserve the distinction between sourced, calculated, simulated, and physically verified results. Do not represent conceptual CAD or synthetic test output as hardware evidence.

Before proposing a change, identify affected recipe, CAD parameter, BOM, documentation, and test boundary. Do not commit secrets, controlled supplier data without permission, generated tool caches, or unreviewed safety claims.

For mechanical changes, regenerate the OpenSCAD STL and note the tool/version. For software changes, run `python -m unittest discover -s tests -v`. Physical-machine changes require an independent safety and validation review by the receiving manufacturer.
