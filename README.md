Python project for uploading files to AWS S3 and Google Cloud Storage.

## Follow the below steps,

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repository/file_uploader.git
   cd file_uploader
   ```

2. Install the module:
   ```bash
   pip install .
   ```

## Usage

To upload files, use the `file_uploader` command followed by the directory path:
```bash
file_uploader /path/to/your/directory
```

## Configuration

Edit the `file_uploader/config.py` file to set your AWS S3 and Google Cloud Storage credentials and bucket names.