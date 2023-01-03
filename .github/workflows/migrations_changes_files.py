name: changed_files
on:  [push]

jobs:

  deploy:
    runs-on: ubuntu-latest
    steps:  
	  
	  - name: Get changed files in the migrations folder
        id: changed-files-specific
        uses: tj-actions/changed-files@v35
        with:
          files: |
            **/migrations/*.py'

      - name: Run step if any file(s) in the migrations folder have been modified
        if: steps.changed-files-specific.outputs.only_modified == 'true'
        run: |
          echo "One or more files in the migrations folder has changed."
          echo "List all the files that have changed: ${{ steps.changed-files-specific.outputs.modified_files }}"
          for file in ${{ steps.changed-files-specific.outputs.modified_files }}; do
                    echo "$file was changed"
          done
		  echo "Aborting the pipeline as migration changed files were detected !"