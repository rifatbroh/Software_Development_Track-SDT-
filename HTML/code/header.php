<!<!DOCTYPE>
<html>
    <head>
        <title>Learning PHP</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>

        <?php 
            function is_active($check) {
                $requested_uri = $_SERVER['REQUEST_URI'];
                $search= strpos($requested_uri, $check);

                if ($search !== false) {
                    return 'active';
                }
            }
        ?>
        <div class="container">
            <div class="header">
                <h1>This is Header</h1>
            </div>
            <div class="main-menu">
                <ul>
                    <li><a class="<?php echo is_active('hello'); ?>" href="hello.php">Home</a></li>
                    <li><a class="<?php echo is_active('about'); ?>" href="about.php">About</a></li>
                    <li><a href="#">Gallery</a></li>
                    <li><a href="#">Support</a></li>
                    <li><a class="<?php echo is_active('contact'); ?>" href="contact.php">Contact</a></li>
                </ul>
            </div>
            <div class="main-content">