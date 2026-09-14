# Frontend boundary

The current local operator surface is served by `software.backend.loomforge.cli serve` to avoid a dependency-only UI scaffold. It presents only stored simulation job history and conspicuously marks the system `SIMULATION ONLY`. A production UI must consume the typed controller API, provide live force/travel plotting, calibration, loading, recovery, and maintenance views, and must never issue arbitrary motion commands.
