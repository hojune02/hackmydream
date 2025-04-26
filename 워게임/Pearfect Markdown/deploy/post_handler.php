<?php
$uploads_dir = 'uploads/';

if ($_SERVER['REQUEST_METHOD'] === 'GET') {

    $file = $_GET['file'] ?? 'example.md';
    $path = $uploads_dir . $file; 

    include($path);
    /*
        Vulnerable part: include() runs the program or outputs the content in the file path provided.
        Hence, if some php program is included in example.md, the program is run.
        In this case, navigating to the root directory and find flag was possible via:
            <?php system("cat /*flag"); ?>
        /*flag wildcard finds all the programs whose names follow the following format: prefix + 'flag', in the root directory.
    */

} else {
    echo "Use GET method!!";
}
?>
