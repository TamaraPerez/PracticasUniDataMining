<?php

	error_log(print_r($_POST,1),3,"/tmp/error.log");
	error_log(print_r($_FILES,1), 3, "/tmp/error.log");

	/**
	 *   upload multiple files to the specified destination directory (which should end with a "/").
	 *   The file names are not altered.
	 *   Fuente: http://html5doctor.com/drag-and-drop-to-server/
 	*/
	function uploadData($dest_dir,$upload_fileset_info, $nombre, $telefono, $email, $libro, $cantidad, $verbose = false)
	{
		foreach ($upload_fileset_info["error"] as $index => $status_code) {
			$name = $upload_fileset_info["name"][$index];
			if ($name == "") {
				continue;	 // If no upload file was given, skip to the next entry
			}

			$type = $upload_fileset_info["type"][$index];
			$tmp_name = $upload_fileset_info["tmp_name"][$index];
			$size = $upload_fileset_info["size"][$index];

			if ($status_code == UPLOAD_ERR_OK) {	// If upload was successful

				$dest_filename = $name;
				$dest_full_path = $dest_dir . $dest_filename . " por ".$nombre;
				// Move the temporary upload file to its desired destination on the server
				move_uploaded_file($tmp_name, "$dest_full_path") or die("ERROR: Couldn't copy the file to the desired destination.");
			}
			else {	 // If upload didn't succeed, spell out the nature of the problem
				echo "Upload FAILED";
			}
		}
	}
	
	$dest_dir = "/var/www/DnD_TAMARA";
	uploadData($dest_dir, $_FILES['fileInput'], $_POST['nombreInput'], $_POST['telefonoInput'], 
		$_POST['emailInput'],$_POST['librosInput'], $_POST['cantLibrosInput']);

