int islandPerimeter(int** grid, int gridRowSize, int gridColSize) {
    int result = 0;
    for (int i= 0; i < gridRowSize; i++)
        for(int j = 0; j < gridColSize; j++){
            int temp = detect(grid, gridRowSize, gridColSize, i, j);
            result += temp;
        }
    return result;
}

int detect(int** grid, int gridRowSize, int gridColSize, int i, int j){
    int temp = 0;
    if (grid[i][j] == 0){
        return 0;
    }

    if ( i == 0 ){
        temp++;
        if (gridRowSize == 1){
            temp++;
        }
        else if (grid[i+1][j] == 0 ){
            temp++;
        }
    }else if ( i == gridRowSize - 1 ){
        temp++;
        if (grid[i-1][j] == 0){
            temp++;
        }
    }else{
        if (grid[i+1][j] == 0){
            temp++;
        }
        if (grid[i-1][j] == 0){
            temp++;
        }
    }

    if (j == 0){
        temp++;
        if (gridColSize == 1){
            temp++;
        }
        else if (grid[i][j+1] == 0 ){
            temp++;
        }
    }else if ( j == gridColSize - 1){
        temp++;
        if (grid[i][j-1] == 0){
            temp++;
        }
    }else{
        if (grid[i][j+1] == 0){
            temp++;
        }
        if (grid[i][j-1] == 0){
            temp++;
        }
    }

    return temp;
}
