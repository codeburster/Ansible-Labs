<?php

/**
 * Configuration for database connection
 *
 */

$host       = "host1.example.com";
$username   = "root";
$password   = "ansible";
$dbname     = "test123";
$dsn        = "mysql:host=$host;dbname=$dbname";
$options    = array(
                PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION
              );
