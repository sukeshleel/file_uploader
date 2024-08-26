import argparse
from file_uploader.uploader import process_files

def main():
    parser = argparse.ArgumentParser(description="Upload files to AWS S3 and Google Cloud Storage.")
    parser.add_argument('directory', type=str, help="Directory to scan for files.")
    args = parser.parse_args()
    
    process_files(args.directory)

if __name__ == "__main__":
    main()