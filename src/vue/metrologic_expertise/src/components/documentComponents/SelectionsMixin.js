var SelevtionsMixin = {
  data () {
    return {
      isModalVisible: false,
      textModalInit: '',
      textModalEdit: '',
      firstEl: '',
      secondEl: '',
      selectedRange: null,
      ccanCreateSpan: false,
    }
  },
  methods: {
    onmousedown (event) {
      this.firstEl = event.target.className
      console.log(event)
    },
    onmouseup (event) {
      this.secondEl = event.target.className
      this.textModalInit = window.getSelection().toString()
      this.textModalEdit = window.getSelection().toString()
      this.isModalVisible = true
      this.highlight()
    },
    getSelectedRange () {
      if (window.getSelection) {
        const sel = window.getSelection()
        if (sel.getRangeAt && sel.rangeCount) {
          this.selectedRange = sel.getRangeAt(0)
        }
      } else if (document.selection) {
        this.selectedRange = document.selection.createRange()
      }
    },
    surroundSelection () {
      const span = document.createElement('span')
      span.className = 'highlight'
      span.style.backgroundColor = '#D05555'
      // span.addEventListener("click", () => {
      //   console.log('click');
      // })
      if (window.getSelection) {
        var sel = window.getSelection()
        if (sel.rangeCount) {
          var range = this.selectedRange.cloneRange()
          range.surroundContents(span)
          sel.removeAllRanges()
          sel.addRange(range)
        }
      }
    },
    highlight () {
      console.log('try to highlight')
      this.getSelectedRange()
      if (this.selectedRange && this.textModalInit) {
        this.surroundSelection()
      }
    }
}