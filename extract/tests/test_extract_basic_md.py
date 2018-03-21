# pylint: skip-file
import os
import json

def test_rmd(script_runner, tmpdir):
    ret = script_runner.run('python3', 'o2rmeta.py', 'extract', 
        '-i', 'extract/tests/carberry',
        '-o', str(tmpdir),
        '-xo', '-m')
    #print(ret.stdout)
    assert ret.success, "process should return success"
    assert ret.stderr == '', "stderr should be empty"
    assert "extracted from: extract/tests/carberry/jc.Rmd" in ret.stdout, " extracted files should be listed"
    assert "total files processed: 1" in ret.stdout, "should process 1 file"
    assert "total extraction errors: 0" in ret.stdout, "should have 0 extraction errors"
    assert "total skipped files: 0" in ret.stdout, "should skip 0 files"

    metadata = json.load(open(os.path.join(str(tmpdir), 'metadata_raw.json')))
    assert metadata['identifier']['doi'] == "10.5555/666655554444"
    assert metadata['keywords'] == ["psychoceramics", "ionian philology"]
    assert metadata['mainfile'] == "jc.Rmd"
    
    assert len(metadata['author']) == 1, "author list has 1 author"
    assert metadata['author'][0]['name'] == "Josiah Stinkney Carberry"
    assert "The implications of" in metadata['description']
    
